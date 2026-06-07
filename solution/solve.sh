#!/bin/bash
cat << 'EOF' | git apply --index
diff --git a/main.py b/main.py
index 8e4f2a1..5f6c7d8 100644
--- a/main.py
+++ b/main.py
@@ -15,9 +15,8 @@ class TaskManager:
     def delete_task(self, task_id):
         # BUG: Off-by-one error after pop() - breaks subsequent ID lookups
-        for i, task in enumerate(self.tasks):
-            if task.id == task_id:
-                self.tasks.pop(i)
-                return True
+        # FIXED: Filter by ID instead of index (stable IDs)
+        self.tasks = [t for t in self.tasks if t.id != task_id]
         return False
EOF

echo "✅ Solution patch applied successfully."
