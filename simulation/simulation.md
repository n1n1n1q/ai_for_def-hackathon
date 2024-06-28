# Adding LEP model
copy `electrical_transmission folder to 
~/gazebo/models/

# Adding custom model in baylands world
in the folder 
<path_to_px4_dir>/Tools/simulation/gazebo-classic/sitl_gazebo-classic/worlds
change file baylands.world
add:
```
<include>
  <uri>model://electrical_transmission</uri>
  <pose>0 0 0 0 0 0</pose>
</include>
```

NOW RUN SIMULATION IN GAZEBO
