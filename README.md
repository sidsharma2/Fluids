# Fluids
Fluid mechanics, thermal transport phenomenon, and basic computational fluid dynamics 
 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 0ca17b58a85dd63f571688846deeaaea2986f676..da57194bd1dc11a717c1eac06985247e70561773 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,7 @@
 # Fluids
-Fluid mechanics, thermal transport phenomenon, and basic computational fluid dynamics 
+
+Fluid mechanics, thermal transport phenomenon, and basic computational fluid dynamics.
+
+This repository now includes `heat2d`, a small Python project for solving a
+steady‑state heat conduction problem on a square plate. See `heat2d/README.md`
+for details.
 
EOF
)
