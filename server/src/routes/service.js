import express from 'express';
import Service from '../models/Service.js';
import { authenticateToken } from '../middleware/auth.js';

const router = express.Router();

// 获取所有服务（公开接口）
router.get('/', async (req, res) => {
  try {
    const { category, active = 'true' } = req.query;
    let query = {};

    if (active === 'true') {
      query.active = true;
    }

    if (category && category !== '全部') {
      query.category = category;
    }

    const services = await Service.find(query).sort({ order: 1, createdAt: -1 });
    res.json(services);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 以下接口需要管理员权限

// 创建服务
router.post('/', authenticateToken, async (req, res) => {
  try {
    const service = new Service(req.body);
    await service.save();
    res.status(201).json({ message: '服务创建成功', service });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 更新服务
router.put('/:id', authenticateToken, async (req, res) => {
  try {
    const service = await Service.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );

    if (!service) {
      return res.status(404).json({ message: '服务不存在' });
    }

    res.json({ message: '服务更新成功', service });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 删除服务
router.delete('/:id', authenticateToken, async (req, res) => {
  try {
    const service = await Service.findByIdAndDelete(req.params.id);

    if (!service) {
      return res.status(404).json({ message: '服务不存在' });
    }

    res.json({ message: '服务删除成功' });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

export default router;
