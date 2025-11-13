import express from 'express';
import Settings from '../models/Settings.js';
import { authenticateToken } from '../middleware/auth.js';

const router = express.Router();

// 获取所有设置（公开接口）
router.get('/', async (req, res) => {
  try {
    const settings = await Settings.find();
    const settingsObj = {};
    settings.forEach(setting => {
      settingsObj[setting.key] = setting.value;
    });
    res.json(settingsObj);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 获取单个设置
router.get('/:key', async (req, res) => {
  try {
    const setting = await Settings.findOne({ key: req.params.key });
    
    if (!setting) {
      return res.status(404).json({ message: '设置不存在' });
    }

    res.json({ key: setting.key, value: setting.value });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 以下接口需要管理员权限

// 创建或更新设置
router.post('/', authenticateToken, async (req, res) => {
  try {
    const { key, value, description } = req.body;

    if (!key || value === undefined) {
      return res.status(400).json({ message: '请提供 key 和 value' });
    }

    let setting = await Settings.findOne({ key });

    if (setting) {
      setting.value = value;
      if (description) setting.description = description;
      await setting.save();
      res.json({ message: '设置更新成功', setting });
    } else {
      setting = new Settings({ key, value, description });
      await setting.save();
      res.status(201).json({ message: '设置创建成功', setting });
    }
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 删除设置
router.delete('/:key', authenticateToken, async (req, res) => {
  try {
    const setting = await Settings.findOneAndDelete({ key: req.params.key });

    if (!setting) {
      return res.status(404).json({ message: '设置不存在' });
    }

    res.json({ message: '设置删除成功' });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

export default router;
