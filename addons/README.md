
# Addons 开发说明

本目录用于存放 Portal50 / Intracity AI 的所有自定义 Odoo 扩展模块（addons）。
外包开发者在进行开发前，请务必阅读本说明。

---

## 1. 目录结构说明

```
addons/
 ├── module_xxx/
 │    ├── __manifest__.py
 │    ├── models/
 │    ├── views/
 │    ├── static/
 │    └── security/
 ├── module_yyy/
 └── README.md
```

命名规范：
- 全小写
- 下划线分隔
- 示例：odoo_quote_pdf

---

## 2. 开发环境要求（必须遵守）

为避免模块在 ODOO 系统中无法运行，开发必须使用以下环境：

### Odoo 版本
- Odoo 18 Enterprise Edition
- 运行方式：从源代码运行（非 Docker）

### Python 版本
- Python 3.13

### 必装依赖模块（避免继承失败）
- sale
- account
- base
- web
- stock

### 文件编码
- UTF-8（禁止 BOM）

### 必须可独立安装
以下命令必须能正常执行且无报错：

```
python3 odoo-bin -i MODULE_NAME -d mydb
```

---

## 3. Odoo 系统集成要求

### a) 禁止修改 Odoo 核心文件
仅允许：
- XML inherit
- Python override
- 新建 model / view

### b) XML xpath 必须唯一明确
禁止模糊 xpath，禁止依赖界面顺序。

---

## 4. 代码提交流程（外包必须遵循）

1. Fork 仓库  
2. 在 addons/ 内创建或更新模块  
3. 发 Pull Request（PR）  
4. PR 内需包含：
   - 改动说明
   - UI / 测试截图
   - 使用说明（如新增字段、菜单路径）

不符合要求的 PR 将被拒绝。

---

## 5. 技术负责人

如需沟通，请联系：

- Technical Lead  
- tech@intracity.ai

---

## 6. 开发注意事项

- 禁止提交以下文件或目录：
  - .idea/
  - .vscode/
  - .DS_Store
  - venv/
- 禁止使用绝对路径
- 禁止添加未经批准的第三方 Python 库
- 所有 PR 必须通过 review 后才能合并
