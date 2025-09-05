# 1️⃣ Přepni se do repozitáře
cd /home/ruda/Dokumenty/Python/gamepie

# 2️⃣ Zkontroluj stav souborů
git status

# 3️⃣ Přidej všechny lokální změny
git add .

# 4️⃣ Commitni změny s popisem
git commit -m "add Messagebox and fix problems"

# 5️⃣ Stáhni vzdálené změny a proveď merge
git pull origin main
# ⚠️ Pokud vzniknou konflikty:
#    a) otevři konfliktní soubory a uprav je podle potřeby
#    b) pak proveď:
#       git add <soubor>
#       git commit -m "Resolve merge conflicts"

# 6️⃣ Pushni změny zpět na GitHub
git push https://github.com/ZeleznaRuda/GamePie-Engine main


