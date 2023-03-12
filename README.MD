# Hospital Management
Este es un módulo introductorio para gestionar los doctores 
y pacientes de un hospital, además de las citas que tienen 
entre ellos. El idioma por defecto es el inglés, pero el español
de España también está disponible, y por tanto, se adaptará si
elegimos ese idioma en Odoo.

## Vistas

Este módulo contiene un menú padre que es <b>Hospital</b>, y dos submenús,
<b>Patients</b>, que contendría elementos relacionados con la gestión de pacientes
, y <b>Staff</b>, que contendría elementos relacionados con los empleados del hospital,
en este caso doctores. 

Dentro de <b>Staff</b>, encontramos el actualmente único elemento, <b>Doctors</b>,
que contiene un registro de los doctores, y permite operaciones básicas
de creación, modificación, borrado, filtrado y agrupaciones.

Dentro de <b>Patients</b> encontramos <b>Patient records</b> que esencialmente muestra
el registro de los pacientes y al igual que en el anterior, permite el mismo
tipo de operaciones. También encontramos el <b>Appointments</b>, que permite
gestionar citas entre pacientes y doctores almacenados.

## Entidades 

### Pacientes
Todos los pacientes tienen información básica almacenada, además de un 
<b>ID <i>secuencial</i></b> generado cuando se almacenan. Todos los pacientes tienen
un doctor asignado, pero pueden tener citas con cualquier doctor.

Cada registro debe ser validado para evitar incongruencias. Específicamente,
controla que la fecha de nacimiento sea válida (en el pasado) y que
la categoría de edad sea consistente con la edad actual (la cual a su vez 
es un campo calculado a través de la fecha de nacimiento).

Adicionalmente, se pueden buscar y agrupar pacientes de acuerdo a variados filtros
relacionados con la información almacenada.

### Doctores

Todos los doctores tienen información básica almacenada con respecto a
su identidad además de su especializad y capacidades. Además, cada registro
genera un <b>ID <i>secuencial</i></b>. Los doctores pueden tener entre 0 y N
pacientes asignados. Adicionalmente, se pueden buscar y agrupar doctores de 
acuerdo a filtros relacionados con género, especialidad y capacidad para la
cirugía.

### Citas

Todas las citas tienen un paciente y un doctor asociado, además de una 
fecha asignada. Cada registro debe ser validado para poder ser insertado
(p. ej, la fecha asignada no puede estar en el pasado).
No es requerido, pero se pueden añadir notas diagnósticas sobre la cita,
además de una prescripción relacionada con la cita. Se pueden filtrar
los resultados por paciente, para ver todas las citas de un paciente determinado,
y también por fechas, si se desea saber qué citas hubo en un día determinado.