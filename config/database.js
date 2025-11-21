import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config({
  path: "./.env",
});

const connectToDB = async () => {
  try {
    const connectToMongoDB = await mongoose.connect(
      `${process.env.MONGO_DB_URI}`
    );
    console.log(
      `MongoDB Database connected ${connectToMongoDB.connection.host}`
    );
  } catch (err) {
    console.log("MongoDB connected failed", err);
    process.exit(1);
  }
};

export default connectToDB;
