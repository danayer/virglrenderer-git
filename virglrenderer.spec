%global commit ba2ba83416b186769f2a00f8fe119ca91de54a18
%global shortcommit ba2ba83




















































































































































































































































































































































































































































































































Name:		virglrenderer
Version:	1.1.525
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
* Tue Aug 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.525-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Mon Aug 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.524-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Mon Aug 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.523-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sun Aug 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.522-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sun Aug 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.521-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sun Aug 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.520-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sat Aug 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.519-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sat Aug 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.518-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Sat Aug 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.517-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Fri Aug 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.516-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Fri Aug 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.515-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Fri Aug 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.514-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Fri Aug 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.513-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Fri Aug 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.512-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Thu Aug 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.511-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Thu Aug 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.510-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Thu Aug 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.509-1.gitba2ba83
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit ba2ba83416b186769f2a00f8fe119ca91de54a18
* Wed Aug 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.508-1.git43ebad0
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 43ebad0ab7d4c3cafe4bf867673af00b5ec3d38e
* Wed Aug 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.507-1.git43ebad0
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 43ebad0ab7d4c3cafe4bf867673af00b5ec3d38e
* Wed Aug 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.506-1.git43ebad0
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 43ebad0ab7d4c3cafe4bf867673af00b5ec3d38e
* Wed Aug 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.505-1.git9622c61
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 9622c613c69a4cac450c1437345918d45e236a07
* Wed Aug 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.504-1.git9622c61
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 9622c613c69a4cac450c1437345918d45e236a07
* Tue Aug 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.503-1.git9622c61
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 9622c613c69a4cac450c1437345918d45e236a07
* Tue Aug 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.502-1.git89982e9
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 89982e9a5e4e6b84c548cc2e5ce8c16face06cc5
* Tue Aug 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.501-1.git423c6f3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 423c6f3fe687093e1327ffd846cff9668c492b1d
* Tue Aug 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.500-1.git423c6f3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 423c6f3fe687093e1327ffd846cff9668c492b1d
* Mon Aug 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.499-1.git423c6f3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 423c6f3fe687093e1327ffd846cff9668c492b1d
* Mon Aug 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.498-1.git423c6f3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 423c6f3fe687093e1327ffd846cff9668c492b1d
* Mon Aug 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.497-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Mon Aug 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.496-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sun Aug 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.495-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sun Aug 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.494-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sun Aug 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.493-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sun Aug 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.492-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sat Aug 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.491-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sat Aug 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.490-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Sat Aug 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.489-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Fri Aug 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.488-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Fri Aug 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.487-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Fri Aug 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.486-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Fri Aug 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.485-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Thu Aug 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.484-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Thu Aug 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.483-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Thu Aug 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.482-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Thu Aug 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.481-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Thu Aug 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.480-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Wed Aug 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.479-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Wed Aug 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.478-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Wed Aug 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.477-1.gitb997bc1
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit b997bc18fafdcb8e563b7b07b54412ea61e12082
* Wed Aug 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.476-1.gitd712297
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d71229702dcb693a8930206366cb8090e31ea28a
* Wed Aug 06 2025 GitHub Actions Bot <actions@github.com> - 1.1.475-1.gitd712297
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d71229702dcb693a8930206366cb8090e31ea28a
* Tue Aug 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.474-1.gitd712297
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit d71229702dcb693a8930206366cb8090e31ea28a
* Tue Aug 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.473-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Tue Aug 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.472-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Tue Aug 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.471-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.470-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.469-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.468-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.467-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.466-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Mon Aug 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.465-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Sun Aug 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.464-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Sun Aug 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.463-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Sat Aug 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.462-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Sat Aug 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.461-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Fri Aug 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.460-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Fri Aug 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.459-1.git765d45d
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 765d45d42929a1e57b502563ab84968c62c1666d
* Fri Aug 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.458-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Aug 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.457-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Aug 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.456-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.455-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.454-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.453-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.452-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 31 2025 GitHub Actions Bot <actions@github.com> - 1.1.451-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.450-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.449-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.448-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.447-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.446-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.445-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.444-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.443-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.442-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.441-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.440-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.439-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.438-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.437-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.436-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.435-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.434-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.433-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.432-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.431-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.430-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.429-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.428-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.427-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.426-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.425-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.424-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.423-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.422-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.421-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.420-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.419-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.418-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.417-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.416-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.415-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.414-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.413-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.412-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.411-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.410-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.409-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.408-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.407-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.406-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.405-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.404-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.403-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.402-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.401-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.400-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.399-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.398-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.397-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.396-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.395-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.394-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.393-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.392-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.391-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.390-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.389-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.388-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.387-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.386-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.385-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.384-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.383-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.382-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.381-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.380-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.379-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.378-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.377-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.376-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.375-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.374-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.373-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.372-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.371-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.370-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.369-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.368-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.367-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.366-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.365-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.364-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.363-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.362-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.361-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.360-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.359-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.358-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.357-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.356-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.355-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.354-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.353-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.352-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.351-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.350-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.349-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.348-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.347-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.346-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.345-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.344-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.343-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sun Jul 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.342-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.341-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.340-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.339-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.338-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.337-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.336-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.335-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.334-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.333-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.332-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.331-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.330-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.329-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.328-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.327-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.326-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.325-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.324-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.323-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.322-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.321-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.320-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Wed Jul 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.319-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.318-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.317-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.316-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.315-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Tue Jul 08 2025 GitHub Actions Bot <actions@github.com> - 1.1.314-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.313-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.312-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.311-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.310-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.309-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.308-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.307-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Mon Jul 07 2025 GitHub Actions Bot <actions@github.com> - 1.1.306-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Sat Jul 05 2025 GitHub Actions Bot <actions@github.com> - 1.1.305-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.304-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.303-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.302-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.301-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.300-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.299-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Fri Jul 04 2025 GitHub Actions Bot <actions@github.com> - 1.1.298-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.297-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.296-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.295-1.git0343d95
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0343d95b63a406c6b1eed256faf7c98ce294c60d
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.294-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.293-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Thu Jul 03 2025 GitHub Actions Bot <actions@github.com> - 1.1.292-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.291-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.290-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.289-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.288-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.287-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Wed Jul 02 2025 GitHub Actions Bot <actions@github.com> - 1.1.286-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Tue Jul 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.285-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Tue Jul 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.284-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Tue Jul 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.283-1.gitf057541
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit f05754119c625149402bd81dda16254edf28d0a0
* Tue Jul 01 2025 GitHub Actions Bot <actions@github.com> - 1.1.282-1.git29c0459
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 29c04591b2388cf5b6627f3b4cda39fa2bdafe2d
* Mon Jun 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.281-1.git29c0459
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 29c04591b2388cf5b6627f3b4cda39fa2bdafe2d
* Mon Jun 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.280-1.git29c0459
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 29c04591b2388cf5b6627f3b4cda39fa2bdafe2d
* Mon Jun 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.279-1.git29c0459
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 29c04591b2388cf5b6627f3b4cda39fa2bdafe2d
* Mon Jun 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.278-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Mon Jun 30 2025 GitHub Actions Bot <actions@github.com> - 1.1.277-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sun Jun 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.276-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sun Jun 29 2025 GitHub Actions Bot <actions@github.com> - 1.1.275-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.274-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.273-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.272-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 28 2025 GitHub Actions Bot <actions@github.com> - 1.1.271-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.270-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.269-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.268-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.267-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 27 2025 GitHub Actions Bot <actions@github.com> - 1.1.266-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.265-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.264-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.263-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.262-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.261-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.260-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 26 2025 GitHub Actions Bot <actions@github.com> - 1.1.259-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.258-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.257-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.256-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.255-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.254-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Wed Jun 25 2025 GitHub Actions Bot <actions@github.com> - 1.1.253-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Tue Jun 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.252-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Tue Jun 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.251-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Tue Jun 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.250-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Tue Jun 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.249-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Tue Jun 24 2025 GitHub Actions Bot <actions@github.com> - 1.1.248-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Mon Jun 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.247-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Mon Jun 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.246-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Mon Jun 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.245-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Mon Jun 23 2025 GitHub Actions Bot <actions@github.com> - 1.1.244-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sun Jun 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.243-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sun Jun 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.242-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sun Jun 22 2025 GitHub Actions Bot <actions@github.com> - 1.1.241-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.240-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.239-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Sat Jun 21 2025 GitHub Actions Bot <actions@github.com> - 1.1.238-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.237-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.236-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.235-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.234-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Fri Jun 20 2025 GitHub Actions Bot <actions@github.com> - 1.1.233-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.232-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.231-1.git0312dc3
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 0312dc34c4cf49f09282e04ac3eeb2cecc4901b5
* Thu Jun 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.230-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Thu Jun 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.229-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Thu Jun 19 2025 GitHub Actions Bot <actions@github.com> - 1.1.228-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Wed Jun 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.227-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Wed Jun 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.226-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Wed Jun 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.225-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Wed Jun 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.224-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Wed Jun 18 2025 GitHub Actions Bot <actions@github.com> - 1.1.223-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Tue Jun 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.222-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Tue Jun 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.221-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Tue Jun 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.220-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Tue Jun 17 2025 GitHub Actions Bot <actions@github.com> - 1.1.219-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Mon Jun 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.218-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Mon Jun 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.217-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Mon Jun 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.216-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Mon Jun 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.215-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Mon Jun 16 2025 GitHub Actions Bot <actions@github.com> - 1.1.214-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Sun Jun 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.213-1.git06d43ce
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 06d43ce974b664f9dc521b706a0ad7f91dbf2866
* Sun Jun 15 2025 GitHub Actions Bot <actions@github.com> - 1.1.212-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Sat Jun 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.211-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Sat Jun 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.210-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Sat Jun 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.209-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Sat Jun 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.208-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Sat Jun 14 2025 GitHub Actions Bot <actions@github.com> - 1.1.207-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Fri Jun 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.206-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Fri Jun 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.205-1.git7a36742
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit 7a367420d0c1115bc83022020fff55d9f0324617
* Fri Jun 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.204-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.203-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Fri Jun 13 2025 GitHub Actions Bot <actions@github.com> - 1.1.202-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.201-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.200-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.199-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.198-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Thu Jun 12 2025 GitHub Actions Bot <actions@github.com> - 1.1.197-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.196-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.195-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.194-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Wed Jun 11 2025 GitHub Actions Bot <actions@github.com> - 1.1.193-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.192-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.191-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.190-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.189-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Tue Jun 10 2025 GitHub Actions Bot <actions@github.com> - 1.1.188-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Mon Jun 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.187-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Mon Jun 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.186-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
* Mon Jun 09 2025 GitHub Actions Bot <actions@github.com> - 1.1.185-1.gita9ed9b5
- Automated update based on changes in mesa-git
- Using latest virglrenderer commit a9ed9b58eab0233ac40ff86fb7b42ee1912a6724
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


