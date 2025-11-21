# Portal50 / Intracity AI — 外包测试任务

本测试任务用于验证外包是否具备基础 Odoo 模块开发能力，以及 GitHub PR 流程是否顺畅。

---

## 任务内容

请在 `addons/` 目录下创建一个新模块：

```
portal50_test_module
```

模块要求如下：

### 1. 创建模型
模型名：`portal50.test.model`

字段：
- `name` (Char)
- `description` (Text)

### 2. 创建菜单
在 Settings 下新增菜单路径：

```
Settings > Portal50 Test > Test Records
```

### 3. 创建视图
为 `portal50.test.model` 创建：

- tree 视图（至少显示 name 字段）
- form 视图（包含 name 和 description）

### 4. 模块可独立安装
以下命令必须能正常执行且不报错：

```
odoo -i portal50_test_module -d testdb
```

---

## 代码提交要求（GitHub PR）

1. Fork 仓库  
   https://github.com/IntracityAI/portal50-odoo-addons

2. 创建开发分支：

```
git checkout -b feature-test-module
```

3. 完成开发后执行：

```
git add .
git commit -m "测试任务：portal50_test_module 完成"
git push -u origin feature-test-module
```

4. 登录 GitHub 发起 Pull Request（PR）

PR 内容必须包含：
- 完成说明
- 模块安装截图
- tree 与 form 视图截图

---

## 注意事项

- 代码必须放在 `addons/portal50_test_module/` 内  
- 不得修改 Odoo 核心模块  
- 模块结构需符合 Odoo 官方规范  
