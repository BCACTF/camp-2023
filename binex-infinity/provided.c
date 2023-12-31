// The following is pseudocode (pseudo C)
// and will not compile on its own

// It is just here to give you a general 
// sense of what the program's code
// looks like

unsigned long hoursGoneBy = 0;
unsigned int distance = 0;
signed int speed = 0;

void loop() {
    print("Hours gone by: %d", hoursGoneBy);
    print("Distance travelled: %u", distance);
    print("Current speed: %d", speed);

    if (distance >= 2 * 1000 * 1000) {
        print("How did you get so far so fast??");
        print("I guess you deserve the flag");

        print_flag();
    }

    if (ask_y_or_no("Do you want to change the speed?")) {
        signed int new_speed = ask_int("Enter new speed: ");

        if (new_speed > 100) {
            print("Haha. That speed is too fast");
            print("Slowing down to 100mph");
            new_speed = 100;
        }

        print("New speed: %d", new_speed);
    }

    print("Driving...");
}

int main() {
    load_flag();

    every_second(loop);
}