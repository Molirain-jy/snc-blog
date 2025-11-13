import express from 'express';
import Blog from '../models/Blog.js';
import { authenticateToken } from '../middleware/auth.js';

const router = express.Router();

// 获取所有文章（公开接口）
router.get('/', async (req, res) => {
  try {
    const { category, search, published = 'true' } = req.query;
    let query = {};

    // 只显示已发布的文章（公开接口）
    if (published === 'true') {
      query.published = true;
    }

    if (category && category !== '全部') {
      query.category = category;
    }

    if (search) {
      query.$or = [
        { title: { $regex: search, $options: 'i' } },
        { excerpt: { $regex: search, $options: 'i' } },
        { content: { $regex: search, $options: 'i' } },
        { tags: { $regex: search, $options: 'i' } }
      ];
    }

    const blogs = await Blog.find(query).sort({ date: -1 });
    res.json(blogs);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 获取单篇文章（公开接口）
router.get('/:id', async (req, res) => {
  try {
    const blog = await Blog.findById(req.params.id);
    
    if (!blog) {
      return res.status(404).json({ message: '文章不存在' });
    }

    res.json(blog);
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 以下接口需要管理员权限

// 创建文章
router.post('/', authenticateToken, async (req, res) => {
  try {
    const blog = new Blog(req.body);
    await blog.save();
    res.status(201).json({ message: '文章创建成功', blog });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 更新文章
router.put('/:id', authenticateToken, async (req, res) => {
  try {
    const blog = await Blog.findByIdAndUpdate(
      req.params.id,
      { ...req.body, updatedAt: Date.now() },
      { new: true }
    );

    if (!blog) {
      return res.status(404).json({ message: '文章不存在' });
    }

    res.json({ message: '文章更新成功', blog });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

// 删除文章
router.delete('/:id', authenticateToken, async (req, res) => {
  try {
    const blog = await Blog.findByIdAndDelete(req.params.id);

    if (!blog) {
      return res.status(404).json({ message: '文章不存在' });
    }

    res.json({ message: '文章删除成功' });
  } catch (error) {
    res.status(500).json({ message: '服务器错误', error: error.message });
  }
});

export default router;
