import express from "express";

const router = express.Router();

router.get("/", (req, res) => {
  return res.send("POST");
});
router.post("/register", (req, res) => {
  const userDetails = req.body;
  return res.send(userDetails);
});
router.put("/", (req, res) => {
  console.log("PUT");
});
router.delete("/", (req, res) => {
  console.log("DELETE");
});

export default router;
