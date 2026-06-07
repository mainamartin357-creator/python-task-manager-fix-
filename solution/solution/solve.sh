#!/bin/bash
# Silver solution script - applies the fix via git patch

cat << 'EOF' | git apply --index
diff --git a/main.py b/main.py
index abc1234..def5678 100644
--- a/main.py
+++ b/main.py
@@ -XX,XX +XX,XX @@ class TaskManager:
     def delete_task(self, task_id):
-        # Broken logic here (off-by-one)
-        for i, task in enumerate(self.tasks):
-            if task['id'] == task_id:
-                self.tasks.pop(i)
-                return True
+        # Fixed: Use list comprehension to filter by ID (stable IDs)
+        self.tasks = [t for t in self.tasks if t['id'] != task_id]
+        return True
EOF

echo "Solution applied successfully."
