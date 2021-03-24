#!/usr/bin/ruby
# coding: utf-8

def divide_y_espera()
  pid = fork()
  if pid.nil?
    # Proceso hijo
    puts "     Soy el proceso hijo. Mi PID es #{$$}"
    sleep(5)
    exit(0)
  else
    # Proceso padre
    puts "Soy el proceso padre. Mi PID es #{$$}"
    puts "El proceso hijo tiene por PID #{pid}"
  end
end

Signal.trap('CLD') do
  puts "Terminó el proceso hijo"
  res = Process.wait
  print "Me dijo que #{res}"
end

5.times {divide_y_espera()}
sleep(10)

exit(0)
