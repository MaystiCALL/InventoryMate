# === Stage 24: Add grouped summaries by category or status ===
# Project: InventoryMate
def generate_grouped_summary(items):
    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        key = f"{item.get('category', 'Uncategorized')} ({item.get('status', 'Unknown')})"
        groups[key].append(item)
    
    summary_lines = ["# Grouped Inventory Summary"]
    total_count = 0
    
    if not groups:
        summary_lines.append("No items found.")
        return "\n".join(summary_lines)
        
    for category_key, group_items in sorted(groups.items()):
        count = len(group_items)
        values = [str(i.get('value', '')) for i in group_items]
        min_val = min([float(v) or 0 for v in values]) if any(float(v) for v in values) else None
        max_val = max([float(v) or 0 for v in values]) if any(float(v) for v in values) else None
        
        summary_lines.append(f"\n## {category_key} ({count} items)")
        
        if min_val is not None:
            summary_lines.append(f"Value Range: ${min_val:.2f} - ${max_val:.2w}")
            
        summary_lines.extend([f"- {i.get('name', 'Unknown')}"] for i in group_items)
    
    total_count = sum(len(v) for v in groups.values())
    summary_lines.append(f"\n# Total Items: {total_count}")
    
    return "\n".join(summary_lines)

# === Stage 24: Add grouped summaries by category or status ===
# Project: InventoryMate
def generate_grouped_summary(items):
    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        key = f"{item.get('category', 'Uncategorized')}: {item.get('status', 'Unknown')}"
        groups[key].append(item)
    
    summary_lines = ["# Grouped Inventory Summary"]
    if not groups:
        summary_lines.append("No items found.")
        return "\n".join(summary_lines)
        
    for category_status, group_items in sorted(groups.items()):
        count = len(group_items)
        total_value = sum(i.get('value', 0) for i in group_items)
        avg_life = sum(i.get('remaining_life_years', 0) for i in group_items) / max(count, 1)
        
        summary_lines.append(f"\n## {category_status} ({count} items)")
        summary_lines.append(f"- Total Value: ${total_value:.2f}")
        summary_lines.append(f"- Avg Remaining Life: ~{avg_life:.1f} years")
        if group_items[0].get('warranty_end'):
            earliest_expiry = min(i.get('warranty_end', 'N/A') for i in group_items)
            latest_expiry = max(i.get('warranty_end', 'N/A') for i in group_items)
            summary_lines.append(f"- Warranty Range: {earliest_expiry} to {latest_expiry}")
            
    return "\n".join(summary_lines)
