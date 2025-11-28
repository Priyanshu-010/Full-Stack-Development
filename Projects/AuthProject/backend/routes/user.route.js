import express from "express"
import { authUser } from "../controller/user.controller.js";

const router = express.Router();

router.post('/auth', authUser)

export default router