import express from "express";
import User from "../schema/userSchema.js";
import bcrypt from "bcrypt";

const saltRounds = 10;

const router = express.Router();

router.get("/:id", async (req, res) => {
  try {
    const user = await User.findOne({ _id: req.params.id });
    if (!user) {
      throw new Error("User not found");
    }
    return res.status(200).send(user);
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

//TODO: add utility functions for error handling amd hashing
router.post("/register", async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (user) {
      throw new Error("User already exists!");
    }
    const userPassword = req.body.password;
    if (!userPassword) {
      throw new Error("User Password Required!");
    }
    if (userPassword.length < 8) {
      throw new Error("Password must be 8 characters or more");
    }
    bcrypt.hash(userPassword, saltRounds, async (err, hash) => {
      if (err) {
        throw new Error("Error Hashing Password");
      }
      const userDetails = {
        ...req.body,
        password: hash,
      };
      const user = await User.create(userDetails);
      return res.status(201).json(user);
    });
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

router.post("/login", async (req, res) => {
  try {
    const { password, username } = req.body;
    if(!password){
      throw new Error("Password is required")
    }
    const user = await User.findOne({ username });
    if (!user) {
      throw new Error("Username not found! Register");
    }

    const match =  await bcrypt.compare(password, user.password);

    if (!match) {
      throw new Error("Password does not match!");
    }
    return res.status(200).send(user);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

router.put("/:id", async (req, res) => {
  try {
    const user = await User.findOneAndUpdate(
      { _id: req.params.id },
      { ...req.body }
    );
    if (!user) {
      throw new Error("User not found");
    }
    return res.status(204).send(user);
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

router.delete("/:id", async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);

    if (!user) {
      throw new Error("User not found");
    }
    return res.status(204).send("User Deleted!!");
  } catch (err) {
    return res.status(500).send({ error: err.message });
  }
});

export default router;
