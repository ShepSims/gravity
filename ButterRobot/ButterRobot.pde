
/* The robot's midpoint */
final int MIDPOINT_X = 100;
final int MIDPOINT_Y = 80;

void setup()
{
  size(200, 200);
  smooth();
  frameRate(30);
}

void draw()
{
  background(255);
  ellipseMode(CENTER);
  fill(color(75));
  rectMode(CENTER);
  
  //Leg
  rect(100, 136, 12, 30); // bottom 
  rect(100, 115, 16, 40); // middle 
  fill(color(150, 150,150)); // top 
  rect(100, 90, 22, 50);
  fill(color(200));
  rect(100, 155, 25, 8);
  fill(color(0));
  rect(86, 155, 8, 12); // wheel
  rect(114, 155, 8, 12); // wheel
  
  // body
  fill(color(200)); 
  rect(100, MIDPOINT_Y, 50, 50); 
  
  // Wire blocks
  fill(color(50, 50, 50));
  rect(86, 52, 4,4);
  rect(96, 52, 4, 4);
  rect(116, 52, 4, 4);
  
  // Wires 
  fill(color(50, 250, 250));
  rect(86, 49, 2, 7);
  fill(color(250, 100, 100));
  rect(96, 49, 2, 7);
  rect(116, 49, 2, 2);

  // Eye
  fill(color(100));
  ellipse(100, MIDPOINT_Y, 36, 36); // outer eye
  ellipse(100, MIDPOINT_Y, 30, 30); // inner eye
  fill(color(0));
  ellipse(100, MIDPOINT_Y, 16, 16); // inner eye
  fill(color(150,200,255));
  ellipse(100, MIDPOINT_Y, 10, 10); // eyeball
  fill(color(255));
  noStroke();
  ellipse(102, MIDPOINT_Y-2, 2, 1);
  drawArms();
}

void drawArms()
{
  fill(color(75));
  rectMode(CORNER);
  
  int len = 60;
  
  rect(63, 70, 10, 60); // left arm
  fill(color(200,200,200));
  rect(63, 100, 10, 4); // elbow
  rect(63, 70, 10, 4); //shoulder
  rect(63, 130, 16, 4); //left hand
  rect(60, 125, 3, 9);
  
  fill(color(75));
  rect(127, 70, 10, 60); // right arm
  fill(color(200,200,200));
  rect(127, 100, 10, 4); // elbow
  rect(127, 70, 10, 4); //shoulder
  rect(122, 130, 16, 4); //left hand
  rect(137, 125, 3, 9);
  
}
