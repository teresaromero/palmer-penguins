var seeds = cat("docker-entrypoint-initdb.d/seed.json");
var MONGO_DBNAME = _getEnv("MONGO_DBNAME");
var MONGO_API_USERNAME = _getEnv("MONGO_API_USERNAME");
var MONGO_API_PASSWORD = _getEnv("MONGO_API_PASSWORD");
var SEED_COLLECTION = _getEnv("SEED_COLLECTION");

db = db.getSiblingDB(MONGO_DBNAME);
db.createCollection(SEED_COLLECTION);
db[SEED_COLLECTION].insertMany(JSON.parse(seeds));

db.createUser({
  user: MONGO_API_USERNAME,
  pwd: MONGO_API_PASSWORD,
  roles: [{ role: "readWrite", db: MONGO_DBNAME }],
});
