 Addons 开发说明

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
