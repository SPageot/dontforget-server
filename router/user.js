import express from "express";
import User from "../schema/userSchema.js";

const router = express.Router();

router.get("/:id", async (req, res) => {
  const user = await User.findOne({ _id: req.params.id });
  console.log(user);
  return res.send(user);
});

router.post("/register", async (req, res) => {
  const user = await User.create(req.body);
  return res.status(201).json(user);
});

router.put("/:id", async (req, res) => {
  const user = await User.findOneAndUpdate(
    { _id: req.params.id },
    { ...req.body }
  );
  return res.send(user);
});

router.delete("/:id", async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);

    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    return res.send("User Deleted!!");
  } catch (err) {
    res.json({ error: err.message });
  }
});

export default router;
