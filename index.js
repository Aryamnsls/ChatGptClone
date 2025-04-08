const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://aryamansingha2:KeiHOCj3g0oqnt0f@cluster0.jriwovf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();
    console.log("✅ Connected to MongoDB");

    const db = client.db("testdb");
    const collection = db.collection("users");

    const result = await collection.insertOne({ name: "Aryaman", status: "active" });
    console.log("Inserted:", result.insertedId);
  } catch (e) {
    console.error(e);
  } finally {
    await client.close();
  }
}

run();
