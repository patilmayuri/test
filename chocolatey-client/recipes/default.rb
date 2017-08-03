#
# Cookbook:: chocolatey-client
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.

powershell_script 'Download file from s3 dochocolatey.0.10.7.nupkg' do
  code <<-EOH
   aws s3 cp s3://arun-cloudfront-logs/windows_packages/chocolatey.0.10.7.nupkg #{ENV['tmp']}/chocolatey.0.10.7.nupkg
  EOH
  not_if { File.exist?("#{ENV['tmp']}\\chocolatey.0.10.7.nupkg") }
end

template "#{ENV['tmp']}/install.ps1" do
  source 'install.ps1.erb'
end

powershell_script 'ExecuteInstalltionFile' do
  cwd  ENV['tmp']
  code <<-EOH
  ./install.ps1
  EOH
end