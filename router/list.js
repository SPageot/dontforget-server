import express from "express";
import List from "../schema/listSchema.js";

const router = express.Router();

router.get("/userList/:id", async (req, res) => {
  try {
    const listId = req.params.id;
    const userList = await List.findOne({ _id: listId });
    return res.send(userList);
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

router.get("/:userId", async (req, res) => {
  try {
    const userId = req.params.userId;
    const userList = await List.find({ userId });
    return res.send(userList);
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

router.post("/create", async (req, res) => {
  try {
    const userList = req.body.list;
    if (userList.listItems.length == 0) {
      throw new Error("Cannot create from empty list");
    }
    const createList = await List.create(userList);
    return res.status(201).send(createList);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

router.put("/:listId", async (req, res) => {
  try {
    const listId = req.params.listId;
    const updateList = await List.findByIdAndUpdate(
      {
        _id: listId,
      },
      {
        ...req.body.list,
      }
    );

    return res.status(200).send(updateList);
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

router.delete("/:listId", async (req, res) => {
  try {
    const listId = req.params.listId;
    const list = await List.findByIdAndDelete({ _id: listId })
    if(list){
    return res.status(201).send({ message: "List Successfully deleted" });
    }else{
      throw new Error("Error deleting list")
    }
  } catch (err) {
    return res.status(500).send(err.message);
  }
});

export default router;
