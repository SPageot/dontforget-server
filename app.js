import express from "express";

const PORT = process.env.PORT;

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  return res.send("test");
});

app.post("/register", async (req, res) => {
  const user = await req.body;
  console.log(user);
  return res.send("sent");
});

app.listen(PORT, (req, res) => {
  console.log("app listening on port 3000");
});
