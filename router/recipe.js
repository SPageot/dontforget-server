import { Router } from "express"
import axios from "axios"

const router = Router()

const N8N_URL = process.env.N8N_API_URL

router.post("/", async (req, res) => {
    const chatInput = req.body.chatInput
    const response = await axios.post(N8N_URL, {
        
            message: `respond only with a recipe for ${chatInput} in an array of objects without instructions`
        
    });
    const recipeDetails = JSON.parse(response.data[0].output.match(/\{[\s\S]*\}|\[[\s\S]*\]/))
    return res.status(200).json(recipeDetails)
})


export default router