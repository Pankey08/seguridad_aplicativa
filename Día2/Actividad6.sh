mkdir /home/kali/bak/;
mkdir /home/kali/herramientas/;
mkdir /home/kali/herramientas/deb/;
mv /home/kali/Downloads/code_1.81.1-1691620686_amd64.deb /home/kali/herramientas/deb/;
cp /home/kali/herramientas/deb/code_1.81.1-1691620686_amd64.deb /home/kali/bak/;
sudo dpkg -i /home/kali/herramientas/deb/code_1.81.1-1691620686_amd64.deb;
echo "todo bien ;)";

