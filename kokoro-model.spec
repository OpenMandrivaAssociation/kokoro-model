Name:		kokoro-model
Version:	1.0
Release:	1
Summary:	Kokoro-82M speech checkpoint
License:	Apache-2.0
Group:		System/Multimedia
URL:		https://huggingface.co/hexgrad/Kokoro-82M
# config.json and kokoro-v1_0.pth from hexgrad/Kokoro-82M.
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
Shared Kokoro-82M checkpoint used by the official kokoro-voice-*
packages. The German Thorsten voice ships its own checkpoint and
does not need this package.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/models/kokoro-v1_0
install -m 644 config.json kokoro-v1_0.pth %{buildroot}%{_datadir}/kokoro/models/kokoro-v1_0/

%files
%{_datadir}/kokoro/models/kokoro-v1_0
