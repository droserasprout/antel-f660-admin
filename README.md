# antel-f660-admin

The Wi-Fi module of ZTE F660 can't provide speeds above 20-30 Mbps, which is ridiculous having 400 Mbps fiber. Optical modems are not as easy to replace as regular routers. So, the most optimal solution is to configure the ISP modem to the bridge mode and use something more suitable as a Wi-Fi AP.

This tiny Python script helps brute-forcing ZTE F660 optical modem WebGUI to acquire admin rights. Built-in credentials are known to be used by Antel, an Uruguayan fiber optic provider.

Default credentials are `user:user`; almost no settings are available there. `installador` account is a bit more powerful but still useless. Our target is `admin`.

## Usage

Firefox Selenium WebDriver must be installed.

```bash
make install
source .venv/bin/activate
python antel_f660_admin.py [http://192.168.1.1]
```

## Configuration

### Modem

In F660 WebGUI:

1. Network -> LAN -> DHCP Server -> Unset Enable DHCP Server
2. Network -> LAN -> DHCP Server -> Set LAN IP Address *192.168.1.100* (e.g.)
3. Network -> WAN -> WAN Connection -> Choose *dhcp_...* -> Delete
4. Network -> WLAN -> Basic -> Wireless RF Mode -> Disabled

### Wi-Fi AP

I'm using Xiaomi Mi Router 4A Gigabit Edition with OpenWrt 22.03.0 on board.

In LuCi:

1. Network -> Interfaces -> LAN -> Edit -> Set IPv4 gateway *192.168.1.100* (e.g.)
