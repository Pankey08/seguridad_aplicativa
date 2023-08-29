scaneo=$(nmap localhost | tail -1 | cut -d " " -f6 | cut -d "(" -f2)

echo "Los host activos son: " $scaneo
