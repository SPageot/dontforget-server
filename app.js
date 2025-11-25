import express from "express";
import connectToDB from "./config/database.js";
import userRouter from "./router/user.js";
import listRouter from "./router/list.js";

const PORT = process.env.PORT;

connectToDB();

const app = express();

app.use(express.json());
app.use("/lists", listRouter);
app.use("/users", userRouter);

app.listen(PORT, (req, res) => {
  console.log("app listening on port 3000");
});
