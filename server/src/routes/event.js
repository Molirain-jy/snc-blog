import express from 'express';
import Event from '../models/Event.js';
import { authenticateToken } from '../middleware/auth.js';

const router = express.Router();

// 获取所有活动（公开接口）
router.get('/', async (req, res) => {
  try {
    const { category, status, published = 'true' } = req.query;
    let query = {};

    if (published === 'true') {
      query.published = true;
    }

    if (category && category !== '全部') {
      query.category = category;
    }

    if (status) {
      query.status = status;
    }

    const events = await Event.find(query).sort({ date: -1 });
    res.json(events);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 获取单个活动
router.get('/:id', async (req, res) => {
  try {
    const event = await Event.findById(req.params.id);
    
    if (!event) {
      return res.status(404).json({ message: '活动不存在' });
    }

    res.json(event);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 以下接口需要管理员权限

// 创建活动
router.post('/', authenticateToken, async (req, res) => {
  try {
    const event = new Event(req.body);
    await event.save();
    res.status(201).json({ message: '活动创建成功', event });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 更新活动
router.put('/:id', authenticateToken, async (req, res) => {
  try {
    const event = await Event.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    if (!event) {
      return res.status(404).json({ message: '活动不存在' });
    }

    res.json({ message: '活动更新成功', event });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 删除活动
router.delete('/:id', authenticateToken, async (req, res) => {
  try {
    const event = await Event.findByIdAndDelete(req.params.id);

    if (!event) {
      return res.status(404).json({ message: '活动不存在' });
    }

    res.json({ message: '活动删除成功' });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

export default router;
