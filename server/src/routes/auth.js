import express from 'express';
import Admin from '../models/Admin.js';
import { generateToken } from '../middleware/auth.js';

const router = express.Router();

// 检查是否已有管理员账号
router.get('/check-setup', async (req, res) => {
  try {
    const adminCount = await Admin.countDocuments();
    res.json({ needsSetup: adminCount === 0 });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 首次设置管理员账号
router.post('/setup', async (req, res) => {
  try {
    const adminCount = await Admin.countDocuments();
    
    if (adminCount > 0) {
      return res.status(400).json({ message: '管理员账号已存在' });
    }

    const { username, password, email } = req.body;

    if (!username || !password || !email) {
      return res.status(400).json({ message: '请提供完整的账号信息' });
    }

    const admin = new Admin({
      username,
      password,
      email,
      isFirstLogin: false
    });

    await admin.save();

    const token = generateToken(admin);

    res.status(201).json({
      message: '管理员账号创建成功',
      token,
      admin: {
        id: admin._id,
        username: admin.username,
        email: admin.email
      }
    });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 登录
router.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;

    if (!username || !password) {
      return res.status(400).json({ message: '请提供用户名和密码' });
    }

    const admin = await Admin.findOne({ username });

    if (!admin) {
      return res.status(401).json({ message: '用户名或密码错误' });
    }

    const isPasswordValid = await admin.comparePassword(password);

    if (!isPasswordValid) {
      return res.status(401).json({ message: '用户名或密码错误' });
    }

    const token = generateToken(admin);

    res.json({
      message: '登录成功',
      token,
      admin: {
        id: admin._id,
        username: admin.username,
        email: admin.email
      }
    });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

export default router;
