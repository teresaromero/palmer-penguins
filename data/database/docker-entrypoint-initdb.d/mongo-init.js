var seeds = cat("docker-entrypoint-initdb.d/seed.json")

db = db.getSiblingDB("palmer-penguins");
db.createCollection("kaggle-penguins-lter")
db['kaggle-penguins-lter'].insertMany(JSON.parse(seeds));
