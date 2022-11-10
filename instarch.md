```
ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
```

```
hwclock --systohc
```

```
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
```

```
echo "apple1" >> /etc/hostname
```

```
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1 localhost" >> /etc/hosts
echo "127.0.1.1 apple1.localdomain apple1" >> /etc/hosts
```

```
pacman -S reflector rsync base-devel
```

```
reflector --country Vietnam --latest 200 --protocol http,https --sort rate --save /etc/pacman.d/mirrorlist
```

```
pacman -S mesa
```

pacman -S networkmanager network-manager-applet dialog wpa_supplicant mtools dosfstools linux-headers
pacman -S avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils inetutils dnsutils bluez bluez-utils cups hplip alsa-utils pipewire pipewire-alsa pipewire-pulse pipewire-jack bash-completion openssh reflector acpi acpi_call tlp virt-manager qemu qemu-arch-extra edk2-ovmf bridge-utils dnsmasq vde2 openbsd-netcat iptables-nft ipset nss-mdns acpid ntfs-3g
#pacman -S sof-firmware
pacman -S kitty terminus-font

pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg

systemctl enable NetworkManager
systemctl enable bluetooth
systemctl enable cups.service
systemctl enable sshd
systemctl enable avahi-daemon
systemctl enable tlp
systemctl enable reflector.timer
systemctl start reflector.timer
#systemctl enable fstrim.timer
#systemctl enable libvirtd
#pacman -S firewalld
#systemctl enable firewalld
systemctl enable acpid

```

```

```

```

```

```

```

```

```

```
