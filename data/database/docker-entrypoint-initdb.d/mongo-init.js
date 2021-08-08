var seeds = JSON.parse(cat("docker-entrypoint-initdb.d/seed.json"));

var MONGO_DBNAME = _getEnv("MONGO_DBNAME");
var MONGO_API_USERNAME = _getEnv("MONGO_API_USERNAME");
var MONGO_API_PASSWORD = _getEnv("MONGO_API_PASSWORD");

db = db.getSiblingDB(MONGO_DBNAME);

db.createCollection("raw-data");

db["raw-data"].insertMany(seeds);

var studynames = db["raw-data"].distinct("studyname");
var studyname_coll = studynames.map((study) => ({ name: study }));

var species = db["raw-data"].distinct("species");
var species_coll = species.map((specie) => ({ name: specie }));

var regions = db["raw-data"].distinct("region");
var region_coll = regions.map((region) => ({ name: region }));

var islands = db["raw-data"].distinct("island");
var island_coll = islands.map((island) => ({ name: island }));

db.createCollection("studynames");
db["studynames"].insertMany(studyname_coll);

db.createCollection("species");
db["species"].insertMany(species_coll);

db.createCollection("regions");
db["regions"].insertMany(region_coll);

db.createCollection("islands");
db["islands"].insertMany(island_coll);

db.createCollection("individuals");

var individuals_cursor = db["raw-data"].aggregate([
  {
    $lookup: {
      from: "studyname",
      localField: "studyname",
      foreignField: "name",
      as: "studyname_id",
    },
  },
  {
    $lookup: {
      from: "island",
      localField: "island",
      foreignField: "name",
      as: "island_id",
    },
  },
  {
    $lookup: {
      from: "region",
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
]);

var individuals_coll = individuals_cursor.toArray();
printjson(individuals_coll);

db["individuals"].insertMany(individuals_coll);

db.createUser({
  user: MONGO_API_USERNAME,
  pwd: MONGO_API_PASSWORD,
  roles: [{ role: "readWrite", db: MONGO_DBNAME }],
});
