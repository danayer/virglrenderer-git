%global commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
%global shortcommit a9ed9b5































































































































































Name:		virglrenderer
Version:	1.1.184
Release:	1.git%{shortcommit}%{?dist}

Summary:	Virgl Rendering library.
License:	MIT

# Updated Source URL to match mesa format
Source:		https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/%{commit}/virglrenderer-%{commit}.tar.gz#/virglrenderer-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python3
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  python3-pyyaml

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files

Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: %{name}%{?_isa} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
# Use a more robust setup approach to handle GitLab's directory naming
%setup -q -n virglrenderer-%{commit}

%build
%ifarch x86_64 aarch64 ppc64 ppc64le s390x
%meson -Dvideo=true -Dvenus=true -Ddrm-renderers=amdgpu-experimental,msm -Dunstable-apis=true -Dvulkan-dload=true -Dminigbm_allocation=true
%else
%meson -Dvideo=true -Dvenus=true -Ddrm-renderers=msm -Dunstable-apis=true -Dvulkan-dload=true -Dminigbm_allocation=true
%endif
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libvirglrenderer.so.1{,.*}
%{_libexecdir}/virgl_render_server

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/libvirglrenderer.so
%{_libdir}/pkgconfig/virglrenderer.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
* Mon Jun 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.184-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sun Jun 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.183-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sun Jun 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.182-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sun Jun 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.181-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sun Jun 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.180-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sat Jun 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.179-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sat Jun 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.178-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sat Jun 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.177-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sat Jun 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.176-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Sat Jun 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.175-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.174-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.173-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.172-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.171-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.170-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.169-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.168-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.167-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.166-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.165-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.164-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.163-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.162-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.161-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.160-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue Jun 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.159-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon Jun 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.158-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon Jun 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.157-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon Jun 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.156-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon Jun 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.155-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon Jun 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.154-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sun Jun 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.153-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sat May 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.152-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.151-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.150-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.149-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.148-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.147-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.146-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.145-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.144-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.143-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.142-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.141-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.140-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.139-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.138-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.137-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.136-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.135-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.134-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.133-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.132-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.131-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.130-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.129-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.128-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.127-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.126-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.125-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sun May 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.124-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sat May 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.123-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sat May 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.122-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.121-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.120-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.119-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.118-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.117-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.116-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Thu May 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.115-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.114-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.113-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.112-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.111-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.110-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.109-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Wed May 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.108-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.107-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.106-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.105-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Tue May 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.104-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.103-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.102-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Mon May 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.101-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sun May 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.100-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sun May 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.99-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sat May 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.98-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Sat May 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.97-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.96-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.95-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.94-1.git07982b4
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 07982b48d1967a007fb6f5ea7eb46400874fcdf1
* Fri May 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.93-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Fri May 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.92-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Thu May 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.91-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Thu May 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.90-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Thu May 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.89-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Thu May 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.88-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Thu May 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.87-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Wed May 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.86-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Wed May 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.85-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Wed May 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.84-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Wed May 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.83-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Wed May 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.82-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Tue May 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.81-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Tue May 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.80-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Tue May 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.79-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Tue May 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.78-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Mon May 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.77-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Mon May 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.76-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Mon May 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.75-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Sun May 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.74-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Sun May 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.73-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Sat May 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.72-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Fri May 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.71-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Fri May 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.70-1.git5c61a6f
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 5c61a6f513b69fcc81e4a65308a0dfb6851307d9
* Fri May 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.69-1.gitd55ff4c
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d55ff4c61f5942180cdc1c442fa1182f01263d3e
* Fri May 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.68-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Thu May 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.67-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Thu May 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.66-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Thu May 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.65-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Thu May 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.64-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Thu May 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.63-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Wed May 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.62-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Wed May 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.61-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Wed May 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.60-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Wed May 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.59-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Tue May 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.58-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Tue May 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.57-1.git630bdf9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 630bdf99a9ba18d32e2503da7b5d42f82eb8fb2f
* Tue May 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.56-1.gita293e78
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a293e78910267b8f480e6f0fe84936d20bd61b44
* Tue May 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.55-1.git71c19e1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 71c19e1c7fa1c2b42ad547dec191085a18d50ecb
* Tue May 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.54-1.git71c19e1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 71c19e1c7fa1c2b42ad547dec191085a18d50ecb
* Mon May 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.53-1.git71c19e1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 71c19e1c7fa1c2b42ad547dec191085a18d50ecb
* Mon May 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.52-1.git71c19e1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 71c19e1c7fa1c2b42ad547dec191085a18d50ecb
* Mon May 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.51-1.git71c19e1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 71c19e1c7fa1c2b42ad547dec191085a18d50ecb
* Mon May 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.50-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Sat May 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.49-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Fri May 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.48-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Fri May 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.47-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Fri May 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.46-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Fri May 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.45-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Thu May 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.44-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Thu May 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.43-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Thu May 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.42-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Wed Apr 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.41-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Wed Apr 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.40-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Wed Apr 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.39-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Wed Apr 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.38-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.37-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.36-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.35-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.34-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.33-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Tue Apr 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.32-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Mon Apr 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.31-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Mon Apr 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.30-1.gitd9f41b8
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d9f41b89fc44e034a11a0596be5a89bb50bdcf65
* Mon Apr 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.29-1.git3b44936
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 3b44936839ab5b5e90bae36c69b12134b972e4d1
* Sat Apr 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.28-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Sat Apr 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.27-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Fri Apr 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.24-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Fri Apr 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.23-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Fri Apr 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.22-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Fri Apr 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.21-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.20-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.19-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.18-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.17-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.16-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Thu Apr 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.15-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Wed Apr 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.14-1.gitdb4fd04
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit db4fd046e0d861048473d8df5b3acabafce4bbc4
* Wed Apr 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.13-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Wed Apr 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.12-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Wed Apr 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.11-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Wed Apr 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.10-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Tue Apr 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.9-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Tue Apr 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.8-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Tue Apr 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.7-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Tue Apr 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.6-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Mon Apr 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.5-1.gitcae17ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit cae17ceea2cc2438bc81824b6dd55825b00f48de
* Wed Apr 02 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.1.4-1.gitcae17ce
- new version, fixes rhbz#2357013

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.1.0-1
- new version

* Sun Sep 01 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.1-5
- Update spec to the latest guidelines

* Tue Aug 06 2024 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-4
- Drop xorg-x11-util-macros dependency as it's not needed anymore

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (#2257772)

* Tue Sep 19 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.0-1
- new version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3.20230104git88b9fe3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2.20230104git88b9fe3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.4-1.20230104git88b9fe3b
- new version

* Mon Sep 12 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.1-1.20220912git19dc97a2
- new version, fixes upstream #286 "Virglrenderer 0.10.1 broke Firefox WebGL rendering in VM"
  Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=2125160

* Tue Sep 06 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.0-2.20220906git62cb845b
- new version, fixes upstream #285 "0.10.0 has issues with fedora 36, hangs the VM"

* Mon Sep 05 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.0-1.20220905gitf70a6640
- new version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.9.1-1.20210420git36391559
- Upstream release 0.9.1. rhbz#1945999

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3.20200212git7d204f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2.20200212git7d204f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.2-1.20200212git7d204f39
- Upstream release 0.8.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2.20191220git66c57963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-1.20191220git66c57963
- Upstream release 0.8.1

* Thu Oct 03 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.0-1.20191002git4ac3a04c
- Latest upstream git snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4.20190424gitd1758cc09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Dave Airlie <airlied@redhat.com> - 0.7.0-3.20190424gitd1758cc09
- Latest upstream git snapshot

* Wed Apr 10 2019 Dave Airlie <airlied@redhat.com> - 0.7.0-3.20180919git402c22886
- build debug package properly, fix make commands

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2.20180919git402c22886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Dave Airlie <airlied@redhat.com> - 0.7.0-1.20180919git402c22886
- upstream 0.7.0 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-5.20170210git76b3da97b
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Dave Airlie <airlied@redhat.com> - 0.6.0-1.git
- upstream 0.6.0 release

* Mon Apr 11 2016 Dave Airlie <airlied@redhat.com> 0.5.0-1.git
- upstream 0.5.0 release

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> 0.4.1-1.git
- fix regression in last build

* Wed Feb 17 2016 Dave Airlie <airlied@redhat.com> 0.4.0-1.git
- latest git snapshot with new API

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3.20151215gite9d3c0c27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dave Airlie <airlied@redhat.com> 0.3.0-2.gite9d3c0c27
- latest upstream to fix gnome-shell rendering bugs

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.3.0-1.20151023git9ce005e5a
- update to latest upstream to fix shader issue

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.2.0-1.20151023git5bfba5190
- update to latest upstream

* Thu Jul 09 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150420gitc4fb40201.2
- fix FTBFS (#1240041)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.20150420gitc4fb40201.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150401gita9ba2c442
- initial virglrenderer spec


