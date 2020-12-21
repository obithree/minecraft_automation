#!/bin/sh

generate_jp_iplist () {
    sed -n 's/^JP\t//p' $1 | while read address; do
        ufw allow from $address to any app $2
    done
}

wget -q -N http://nami.jp/ipv4bycc/cidr.txt.gz -O /tmp/cidr.txt.gz
gunzip -q -f -c /tmp/cidr.txt.gz > /tmp/cidr.txt

if [ -f /tmp/cidr.txt ]; then
    generate_jp_iplist /tmp/cidr.txt Minecraft
fi

rm -f /tmp/cidr.txt
rm -f /tmp/cidr.txt.gz
