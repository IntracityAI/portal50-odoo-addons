# 🚀 Portal50 Odoo Addons — Developer Guide（外包开发指南）
**Intracity AI Technology Ltd.**

本仓库用于 **Portal50** 平台的所有自定义 Odoo 模块（addons）。  
外包开发者请严格按照本文件的流程提交代码。

---

# 📂 1. 仓库结构说明

```plaintext
portal50-odoo-addons/
│
├── addons/                         # 所有自定义模块放在这里
│   └── example_module/             # 示例模块
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   └── example_model.py
│       └── views/
│           └── example_view.xml
│
├── docs/                           # 开发文档 / 客户需求文档
│   ├── developer_guide.md
│   └── requirements/
│       └── sale_order_customization.md
│
├── .github/
│   └── pull_request_template.md    # PR 模版（强制要求）
│
├── .gitignore
└── README.md
```

---

# 👤 2. 开发流程概述

所有外包开发必须：

✔ 在 **dev 分支** 上开发  
✔ 每个功能模块独立提交  
✔ 所有 PR 必须符合 PR 模版  
✔ PR 通过后由仓库管理员合并到 main  
✔ **禁止直接向 main 推送**

---

# 🌱 3. 分支规范

| 分支 | 用途 |
|------|------|
| **main** | 稳定版本，只能通过 PR 合并 |
| **dev** | 外包统一开发分支 |
| feature/xxx | 大型功能可使用的临时分支（可选） |

---

# 🏗 4. 开发任务的交付方式

每一个开发任务会包含：

1. 功能描述  
2. 业务逻辑说明  
3. 验收条件（Acceptance Criteria）

外包需要：

✔ 根据说明在 `addons/` 下创建对应模块  
✔ 修改现有模块也必须走 Pull Request  
✔ 提交前务必自测通过  

---

# 🛠 5. Odoo 模块开发规范

### 1）模块结构必须正确

```
module_name/
  ├── __init__.py
  ├── __manifest__.py
  ├── models/
  ├── views/
  ├── security/
  └── static/
```

### 2）Python 代码规范

- 使用 Odoo ORM（禁止 Raw SQL）
- 遵守 PEP8
- 类名必须匹配 Model 名（增强可读性）
- 业务逻辑必须写注释

### 3）XML 视图规范

- 使用 `xpath` 继承
- 禁止复制大段现成代码
- ID 必须唯一，推荐：`module_name.view_xxx`

### 4）Manifest 规范

示例：

```python
{
    'name': 'Portal50 - Example',
    'author': 'Intracity AI Technology Ltd.',
    'version': '1.0.0',
    'depends': ['base'],
    'data': [
        'views/example_view.xml'
    ],
}
```

---

# 🔍 6. Pull Request（PR）规范

所有 PR 必须遵循 `.github/pull_request_template.md` 模版。

### 提交前确认：

✔ 每个 PR 只做一件事（Single Purpose）  
✔ 本地测试全部通过  
✔ 附上必要截图（界面改动时必须有）  
✔ 改动最小化、可读性强  

---

# 🧪 7. 本地环境要求

外包本地需要：

- Odoo 18（Enterprise 或 Community）
- Python 3.10+
- PostgreSQL 14+
- 能正常运行 Portal50 自定义 addons

### addons 加载路径示例：

```bash
addons_path = /path/to/odoo/addons,/path/to/portal50-odoo-addons/addons
```

---

# 🧷 8. 代码提交方式（外包强制使用）

所有外包都必须通过 Git 提交代码：

```bash
git checkout dev
git add .
git commit -m "Feature: XXX"
git push origin dev
```

Push 后即可在 GitHub 建立 PR。

---

# 🧹 9. 代码 Review 标准

| 项目 | 要求 |
|------|------|
| 功能正确 | 按需求实现，无偏差 |
| 代码质量 | 模块化、可维护、命名规范 |
| 结构正确 | 所有文件放对目录 |
| 安全性 | 不破坏已有模块 |
| 兼容性 | 必须兼容 Odoo 18 |

---

# 📝 10. 联系方式与支持

若有任何问题，请通过：

- GitHub Issue  
- 微信:kyostarsunson
- 闲鱼:Intracity

# 🎯 最终目标

我们追求：

- 长期合作  
- 高可靠性  
- 可维护的模块化架构  
- 清晰透明的开发流程  
- 构建 Portal50 的完整 Odoo 生态系统  


