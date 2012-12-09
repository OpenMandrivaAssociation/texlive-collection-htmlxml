# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-htmlxml
Epoch:		1
Version:	20120224
Release:	1
Summary:	HTML/SGML/XML support
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-htmlxml.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-jadetex
Requires:	texlive-passivetex
Requires:	texlive-tex4ht
Requires:	texlive-xmlplay
Requires:	texlive-xmltex
Requires:	texlive-collection-basic
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-latex

%description
Packages to convert LaTeX to XML/HTML, and typset XML/SGML.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780328
- Update to latest release.
- Import texlive-collection-htmlxml
- Import texlive-collection-htmlxml

