%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name excon

Summary: Http(s) EXtended CONnections
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.39.6
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/excon
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: ca-certificates
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: ca-certificates
# For the tests
# We do not have everything in scl
#BuildRequires: %{?scl_prefix_ror}rubygem(activesupport)
#BuildRequires: %{?scl_prefix_ror}rubygem(delorean)
#BuildRequires: %{?scl_prefix_ror}rubygem(open4)
#BuildRequires: %{?scl_prefix_ror}rubygem(shindo)
#BuildRequires: %{?scl_prefix_ror}rubygem(sinatra)
#BuildRequires: %{?scl_prefix_ror}rubygem(eventmachine)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
EXtended http(s) CONnections

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# kill bundled cacert.pem
ln -sf %{_sysconfdir}/pki/tls/cert.pem \
       %{buildroot}%{gem_instdir}/data/cacert.pem

# We do not have all deps
#%%check
#pushd .%{gem_instdir}
# Don't use Bundler.
#sed -i "/'bundler\/setup'/ s/^/#/" tests/test_helper.rb

# Unicorn is not available in Fedora yet (rhbz#1065685).
#sed -i '/with_unicorn/ s/^/  pending\n\n/' tests/basic_tests.rb

#shindo
#popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.md
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile*
%{gem_spec}

%files doc
%doc %{gem_instdir}/CONTRIBUT*
%doc %{gem_instdir}/README.md
%{gem_instdir}/benchmarks
%{gem_instdir}/tests
%{gem_instdir}/excon.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/changelog.txt

%changelog
* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 0.39.6-2
- Add SCL macros

* Mon Sep 29 2014 Brett Lentz <blentz@redhat.com> - 0.39.6-1
- Update to excon 0.39.6.

* Wed Jul 30 2014 Brett Lentz <blentz@redhat.com> - 0.38.0-1
- Update to excon 0.38.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Vít Ondruch <vondruch@redhat.com> - 0.33.0-1
- Update to excon 0.33.0.

* Wed Oct 09 2013 Josef Stribny <jstribny@redhat.com> - 0.25.3-1
- Update to excon 0.25.3.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Vít Ondruch <vondruch@redhat.com> - 0.21.0-1
- Update to excon 0.21.0.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 0.16.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 09 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.16.7-1
- Update to Excon 0.16.7.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.3-1
- Update to Excon 0.14.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-1
- Update to Excon 0.14.1
- Removed no longer needed patch for downgrading dependencies.
- Remove newly bundled certificates and link to system ones.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-2
- Fixed the changelog.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-1
- Update to version 0.9.5
- Fixed the dependencies for the new version.

* Mon Dec 05 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.12-1
- Update to version 0.7.12.

* Mon Nov 28 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.8-1
- Update to version 0.7.8.
- Replaced defines with more appropriate globals.
- Added Build dependency on rubygem-eventmachine.
- Fixed running tests for the new version.

* Wed Oct 12 2011 bkabrda <bkabrda@redhat.com> - 0.7.6-1
- Update to version 0.7.6
- Introduced doc subpackage
- Introduced check section

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.6.3-1
- Initial package
