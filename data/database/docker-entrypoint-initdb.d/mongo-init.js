var seeds = JSON.parse(cat("docker-entrypoint-initdb.d/seed.json"));
var species_json = JSON.parse(cat("docker-entrypoint-initdb.d/species.json"));

var MONGO_DBNAME = _getEnv("MONGO_DBNAME");
var MONGO_API_USERNAME = _getEnv("MONGO_API_USERNAME");
var MONGO_API_PASSWORD = _getEnv("MONGO_API_PASSWORD");

db = db.getSiblingDB(MONGO_DBNAME);

db.createCollection("kaggle-raw-data");
db["kaggle-raw-data"].insertMany(seeds);

db.createCollection("ng-species-raw-data");
db["ng-species-raw-data"].insertMany(species_json);

var studynames = db["kaggle-raw-data"].distinct("studyname");
var studyname_coll = studynames.map((study) => ({ name: study }));

var kaggle_species = db["kaggle-raw-data"].aggregate([
  {
    $project: {
      species: 1,
      common_name: 1,
      scientific_name: 1,
      _id: 0,
    },
  },
  {
    $group: {
      _id: {
        species: "$species",
        common_name: "$common_name",
        scientific_name: "$scientific_name",
      },
    },
  },
  {
    $project: {
      _id: 0,
      name: "$_id.species",
      common_name: "$_id.common_name",
      scientific_name: "$_id.scientific_name",
    },
  },
]);

db.createCollection("species");
db["species"].insertMany(kaggle_species.toArray());

var complete_species = db["species"]
  .aggregate([
    {
      $lookup: {
        from: "ng-species-raw-data",
        localField: "common_name",
        foreignField: "common_name",
        as: "data",
      },
    },
    {
      $unwind: {
        path: "$data",
      },
    },
    {
      $project: {
        name: 1,
        scientific_name: 1,
        common_name: 1,
        type: "$data.type",
        diet: "$data.diet",
        group_name: "$data.group_name",
        average_life_span_in_the_wild: "$data.average_life_span_in_the_wild",
        size: "$data.size",
        weight: "$data.weight",
        iucn_red_list_status: "$data.iucn_red_list_status",
        current_population_trend: "$data.current_population_trend",
        source_url: "$data.source_url",
      },
    },
  ])
  .toArray();

complete_species.forEach((specie) => {
  var _id = specie._id;
  db["species"].findOneAndUpdate({ _id }, { $set: specie });
});

var regions = db["kaggle-raw-data"].distinct("region");
var region_coll = regions.map((region) => ({ name: region }));

var islands = db["kaggle-raw-data"].distinct("island");
var island_coll = islands.map((island) => ({ name: island }));

db.createCollection("studynames");
db["studynames"].insertMany(studyname_coll);

db.createCollection("regions");
db["regions"].insertMany(region_coll);

db.createCollection("islands");
db["islands"].insertMany(island_coll);

db.createCollection("individuals");

var individuals_cursor = db["kaggle-raw-data"]
  .aggregate([
    {
      $lookup: {
        from: "studynames",
        localField: "studyname",
        foreignField: "name",
        as: "studyname_id",
      },
    },
    {
      $lookup: {
        from: "islands",
        localField: "island",
        foreignField: "name",
        as: "island_id",
      },
    },
    {
      $lookup: {
        from: "regions",
        localField: "region",
        foreignField: "name",
        as: "region_id",
      },
    },
    {
      $lookup: {
        from: "species",
        localField: "species",
        foreignField: "name",
        as: "species_id",
      },
    },
    {
      $project: {
        island: 0,
        studyname: 0,
        species: 0,
        region: 0,
        _id: 0,
      },
    },
    {
      $unwind: {
        path: "$studyname_id",
      },
    },
    {
      $unwind: {
        path: "$island_id",
      },
    },
    {
      $unwind: {
        path: "$region_id",
      },
    },
    {
      $unwind: {
        path: "$species_id",
      },
    },
    {
      $set: {
        studyname_id: "$studyname_id._id",
        island_id: "$island_id._id",
        region_id: "$region_id._id",
        species_id: "$species_id._id",
        date_egg: {
          $dateFromString: {
            dateString: "$date_egg",
          },
        },
      },
    },
  ])
  .toArray();

db["individuals"].insertMany(individuals_cursor);

db.createUser({
  user: MONGO_API_USERNAME,
  pwd: MONGO_API_PASSWORD,
  roles: [{ role: "readWrite", db: MONGO_DBNAME }],
});
