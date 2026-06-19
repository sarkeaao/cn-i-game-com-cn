# tools/site_summary.py

import json
from datetime import datetime

# 内置站点资料库
SITE_DATA = [
    {
        "name": "爱游戏中心",
        "url": "https://cn-i-game.com.cn",
        "keywords": ["爱游戏", "游戏平台", "休闲娱乐"],
        "tags": ["游戏", "娱乐", "在线"],
        "description": "提供丰富多样的在线游戏，满足不同玩家需求，打造极致娱乐体验。"
    },
    {
        "name": "游戏资讯站",
        "url": "https://news.game-example.com",
        "keywords": ["游戏新闻", "攻略", "评测"],
        "tags": ["资讯", "攻略", "评测"],
        "description": "最新游戏动态、深度评测与实用攻略一网打尽。"
    },
    {
        "name": "开发者社区",
        "url": "https://dev.game-community.cn",
        "keywords": ["游戏开发", "技术交流", "开源"],
        "tags": ["开发", "社区", "技术"],
        "description": "游戏开发者交流平台，分享技术经验与开源项目。"
    }
]

def format_summary(site: dict) -> str:
    """生成单条站点的结构化摘要"""
    lines = [
        f"站点名称: {site['name']}",
        f"URL: {site['url']}",
        f"关键词: {', '.join(site['keywords'])}",
        f"标签: {', '.join(site['tags'])}",
        f"说明: {site['description']}",
        "---"
    ]
    return "\n".join(lines)

def generate_full_summary(sites: list) -> str:
    """生成完整摘要报告"""
    header = (
        f"站点摘要报告\n"
        f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"站点总数: {len(sites)}\n"
        + "=" * 40 + "\n"
    )
    body = "\n".join(format_summary(s) for s in sites)
    return header + body

def export_to_json(sites: list, filepath: str = "site_summary.json") -> None:
    """将摘要导出为 JSON 文件"""
    export_data = []
    for site in sites:
        export_data.append({
            "name": site["name"],
            "url": site["url"],
            "keywords": site["keywords"],
            "tags": site["tags"],
            "description": site["description"],
            "generated_at": datetime.now().isoformat()
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    print(f"已导出至: {filepath}")

def main():
    """主函数：显示摘要并导出"""
    summary = generate_full_summary(SITE_DATA)
    print(summary)
    export_to_json(SITE_DATA)

if __name__ == "__main__":
    main()