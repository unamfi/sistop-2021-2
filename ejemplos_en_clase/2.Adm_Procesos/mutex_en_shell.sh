#!/bin/bash
#
# Ejemplo de invocación:
#
# for i in hugo paco luis rico donald y todos los demas; do ./mutex_en_shell.sh; done
LOCK=/tmp/no_te_entumas

echo "Este es el proceso $$"

sleep 0.1

lockfile $LOCK
echo "Entrando a mi sección crítica... ($$)"

sleep 0.2
echo "Saliendo de mi sección crítica ($$)"
rm -f $LOCK

