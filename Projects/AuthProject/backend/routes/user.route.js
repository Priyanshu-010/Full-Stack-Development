import express from "express"
import { authUser } from "../controller/user.controller.js";

const router = express.Router();

router.post('/auth', authUser)
router.post('/login', authUser)
router.post('/register', authUser)

export default router