function solution(a, b) {
    const dayOfTheWeek = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    const month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    };
    
    let sumValue = b;
    for (let i = 1; i < a; i++) {
        sumValue += month[i];
    }
    
    return dayOfTheWeek[sumValue % 7];
}