public class Guard {
    public int id;

    int[] sleepingTime;

    public Guard(int id) {
        this.id = id;
        sleepingTime = new int[60];
    }

    public int totalAsleep() {
        int acc = 0;
        for (int i = 0; i < 60; i++) {
            acc += sleepingTime[i];
        }
        return acc;
    }

    public int highestMinute() {
        int max = 0;
        int maxMinute = 0;
        for (int i = 0; i < 60; i++) {
            if (sleepingTime[i] > max) {
                max = sleepingTime[i];
                maxMinute = i;
            }
        }
        return maxMinute;
    }

    public int calculateValue() {
        return id * highestMinute();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("#");
        sb.append(id);
        sb.append(":\t");
        for (int i = 0; i < 60; i++) {
            sb.append(sleepingTime[i]);
            sb.append("\t");
        }
        sb.append("Minutes asleep: ");
        sb.append(totalAsleep());
        sb.append("\t");
        sb.append("Highest minute:");
        sb.append(highestMinute());
        sb.append("\t");
        sb.append("Total:");
        sb.append(calculateValue());
        return sb.toString();
    }
}
