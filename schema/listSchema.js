import mongoose from "mongoose";

const listSchema = mongoose.Schema({
  userId: String,
  title: String,
  listItems: [String],
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

export default mongoose.model("List", listSchema);
