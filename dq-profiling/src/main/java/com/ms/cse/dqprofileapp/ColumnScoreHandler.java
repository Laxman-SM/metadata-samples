package com.ms.cse.dqprofileapp;

import com.microsoft.azure.functions.ExecutionContext;
import com.microsoft.azure.functions.annotation.FunctionName;
import com.microsoft.azure.functions.annotation.TimerTrigger;
import com.ms.cse.dqprofileapp.extensions.TimestampExtension;
import com.ms.cse.dqprofileapp.models.FunctionInput;
import com.ms.cse.dqprofileapp.models.ScheduleStatus;
import org.springframework.cloud.function.adapter.azure.AzureSpringBootRequestHandler;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan(basePackages={"com.ms.cse.dqprofileapp"})
public class ColumnScoreHandler extends AzureSpringBootRequestHandler<FunctionInput, Integer> {
    @FunctionName("updateColumnScores")
    public Integer execute(
            @TimerTrigger(name = "updateColumnScoresTrigger", schedule = "0 */30 * * * *") String timerInfo,
            ExecutionContext context) {
        ScheduleStatus scheduleStatus = ScheduleStatus.Deserialize(timerInfo);
        FunctionInput input = new FunctionInput();
        input.setTimeStamp(scheduleStatus.getLast() == null ? TimestampExtension.now() : scheduleStatus.getLast());
        input.setExecutionContext(context);
        return handleRequest(input, context);
    }
}