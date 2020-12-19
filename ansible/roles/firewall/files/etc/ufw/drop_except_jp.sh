#!/bin/sh

generate_iptabels_cmd () {
    iptables_path=/sbin/iptables
    # EXCLUDE_PORTS=80,443,25
    echo $iptables_path -F DROP_EXCEPT_JP
    # echo /sbin/iptables -A DROP_EXCEPT_JP -p tcp -m multiport --dport $EXCLUDE_PORTS -m state --state NEW -j RETURN
    echo $iptables_path -A DROP_EXCEPT_JP -s 192.168.10.0/24 -j RETURN
    sed -n 's/^JP\t//p' $1 | while read address; do
        echo $iptables_path -A DROP_EXCEPT_JP -s $address -j RETURN
    done
    echo $iptables_path -A DROP_EXCEPT_JP -j DROP
}

wget -q -N http://nami.jp/ipv4bycc/cidr.txt.gz -O /tmp/cidr.txt.gz
gunzip -q -f -c /tmp/cidr.txt.gz > /tmp/cidr.txt

if [ -f /tmp/cidr.txt ]; then
    generate_iptabels_cmd /tmp/cidr.txt > /etc/ufw/after.init.drop_except_jp
fi

rm -f /tmp/cidr.txt
rm -f /tmp/cidr.txt.gz
