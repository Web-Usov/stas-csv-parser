abstract class CsvReport<R = any> {
  abstract generate(rows: Array<Record<string, any>>): Map<string, R>;
}

/*
  [{student: "vasa", coffee_spent: 100},
   {student: "petya", coffee_spent: 200},
   {student: "vasa", coffee_spent: 300},
   {student: "petya", coffee_spent: 400},
   {student: "misha", coffee_spent: 500},
   {student: "misha", coffee_spent: 600},
   {student: "misha", coffee_spent: 700},
   {student: "misha", coffee_spent: 800},
   {student: "misha", coffee_spent: 900},
   {student: "misha", coffee_spent: 1000},
   {student: "misha", coffee_spent: 1100},
   {student: "misha", coffee_spent: 1200},
  ]
*/

class MaxCoffeeReport implements CsvReport<number> {
  static reportName = "max" as const;
  generate(rows: Array<Record<string, string>>): Map<string, number> {
    const maxCoffeeByStud = new Map<string, number>();
    for (const row of rows) {
      const student = row.student;
      const coffee_spent = parseInt(row.coffee_spent);
      maxCoffeeByStud.set(
        student,
        Math.max(maxCoffeeByStud.get(student) || 0, coffee_spent)
      );
    }
    return maxCoffeeByStud;
  }
}

class AverageCoffeeReport {}

// main.ts

// const Reports = {
//   [MaxCoffeeReport.name]: MaxCoffeeReport,
// } as const;

// const getReport = (name: keyof typeof Reports): new () => CsvReport => {
//   const report = Reports[name];
//   return report;
// };

type ReportConstructor<Name extends string = string, R = any> = {
  new (): CsvReport<R>;
  reportName: Name;
};

class ReportManager<Reports extends readonly ReportConstructor[]> {
  private reports: Map<Reports[number]["reportName"], Reports[number]> =
    new Map();

  constructor(reports: Reports) {
    for (const report of reports) {
      this.reports.set(report.reportName, report);
    }
  }

  public getReport<Name extends Reports[number]["reportName"]>(
    name: Name
  ): Extract<Reports[number], { reportName: Name }> {
    const report = this.reports.get(name);
    if (!report) {
      throw new Error(`Report ${name} not found`);
    }
    return report as Extract<Reports[number], { reportName: Name }>;
  }
}

const reportManager = new ReportManager([MaxCoffeeReport] as const);
const report = reportManager.getReport("max");
console.log(report);
