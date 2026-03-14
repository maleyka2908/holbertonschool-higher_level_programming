cd /tmp/
curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
nano 4-hidden_discovery.py
#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Modulun daxilindəki bütün adları alırıq
    names = dir(hidden_4)
    
    # Adları əlifba sırası ilə düzürük və "__" ilə başlamayanları seçirik
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
          chmod u+x 4-hidden_discovery.py
./4-hidden_discovery.py
