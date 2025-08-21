"""
Wowza Log Analysis Prompts
"""

class WowzaAnalysisPrompts:
    """Class containing prompt templates for analyzing Wowza logs"""
    
    @staticmethod
    def get_all_prompts():
        """Return dictionary containing all 6 detailed prompts"""
        return {
            "error_classification": WowzaAnalysisPrompts.error_classification_prompt(),
            # "codec_issues_analysis": WowzaAnalysisPrompts.codec_issues_prompt(),
            # "streaming_performance": WowzaAnalysisPrompts.streaming_performance_prompt(),
            # "transcoding_analysis": WowzaAnalysisPrompts.transcoding_analysis_prompt(),
            # "timeline_analysis": WowzaAnalysisPrompts.timeline_analysis_prompt(),
            # "comprehensive_solution": WowzaAnalysisPrompts.comprehensive_solution_prompt()
        }
    
    @staticmethod
    def get_simple_prompts():
        """Return dictionary containing 3 basic prompts for quick analysis"""
        return {
            "main_errors": "What are the main errors in these Wowza logs? Please list the top 5 most important errors with their frequency.",
            "root_causes": "What are the root causes of the errors found in these Wowza logs? Explain why these problems occurred.",
            "solutions": "What are the specific solutions to fix the errors in these Wowza logs? Provide step-by-step instructions."
        }
    
    @staticmethod
    def error_classification_prompt():
        """Prompt 1: Error classification and statistics"""
        return """
Analyze the Wowza logs and classify errors systematically.

TASK REQUIREMENTS:
1. Error Classification:
   - Count each type of error (server, codec, streaming, etc.)
   - Identify severity levels (CRITICAL, ERROR, WARN, INFO)
   - Group by functionality (transcoding, streaming, codec, connection)

2. Statistical Analysis:
   - List top 5 most frequent errors
   - Calculate percentage distribution of error types
   - Assess severity impact on system performance

3. System Health Assessment:
   - Overall system status evaluation
   - Priority issues that need immediate attention
   - Impact assessment on user experience

Return JSON format:
```json
{
  "summary": {
    "total_errors": 0,
    "error_categories": {
      "codec": 0,
      "streaming": 0,
      "server": 0,
      "transcoding": 0
    },
    "severity_distribution": {
      "critical": 0,
      "error": 0,
      "warn": 0,
      "info": 0
    }
  },
  "top_errors": [
    {
      "error_type": "string",
      "count": 0,
      "severity": "string",
      "description": "string"
    }
  ],
  "priority_issues": ["string"],
  "system_health_score": 85
}
```
"""

    @staticmethod
    def codec_issues_prompt():
        """Prompt 2: Codec and streaming issues analysis"""
        return """
Analyze codec-related problems in the Wowza logs.

FOCUS AREAS:
1. Codec Compatibility Issues:
   - H264/OPUS compatibility problems
   - Invalid audio/video codec combinations
   - HLS (HTTP Live Streaming) packager errors
   - Codec decode/encode failures

2. Stream Packetization Problems:
   - Audio/video packetization failures
   - Stream format mismatches
   - Codec configuration errors
   - Reserved bits decode issues

3. Root Cause Analysis:
   - Identify underlying causes for each codec issue
   - Assess impact on streaming quality
   - Find relationships between different codec errors

4. Solutions and Recommendations:
   - Specific fixes for each codec problem
   - Optimal codec configuration settings
   - Best practices to prevent future issues

Return JSON format:
```json
{
  "codec_issues": {
    "h264_opus_conflicts": [
      {
        "issue": "string",
        "frequency": 0,
        "impact": "string"
      }
    ],
    "hls_compatibility": ["string"],
    "packetization_errors": ["string"]
  },
  "root_causes": [
    {
      "cause": "string",
      "affected_areas": ["string"],
      "severity": "string"
    }
  ],
  "impact_assessment": {
    "stream_quality": "string",
    "user_experience": "string",
    "system_performance": "string"
  },
  "solutions": [
    {
      "problem": "string",
      "solution": "string",
      "implementation": "string"
    }
  ],
  "recommended_settings": {
    "codec_config": {},
    "streaming_params": {}
  }
}
```
"""

    @staticmethod
    def streaming_performance_prompt():
        """Prompt 3: Streaming performance evaluation"""
        return """
Evaluate streaming performance and quality metrics from the logs.

ANALYSIS AREAS:
1. Performance Metrics:
   - Stream duration issues and chunk problems
   - Target duration vs actual duration discrepancies
   - Stream discontinuity events
   - Buffer underruns and latency problems

2. Stream Quality Assessment:
   - Keyframe alignment issues
   - Chunk duration out of acceptable bounds
   - Audio/video synchronization problems
   - Quality degradation indicators

3. Transcoding Performance:
   - Transcoding pipeline efficiency
   - Resource utilization patterns
   - Processing bottlenecks identification
   - Encoding/decoding delays

4. User Experience Impact:
   - Playback interruptions and stalls
   - Buffering frequency and duration
   - Stream stability and reliability
   - Quality consistency across different bitrates

Return JSON format:
```json
{
  "performance_metrics": {
    "average_chunk_duration": 0.0,
    "discontinuity_rate": 0.0,
    "keyframe_issues_count": 0,
    "buffer_underruns": 0
  },
  "quality_indicators": {
    "sync_issues": 0,
    "quality_drops": 0,
    "stability_score": 0
  },
  "bottlenecks": [
    {
      "type": "string",
      "severity": "string",
      "description": "string",
      "suggested_fix": "string"
    }
  ],
  "user_experience_score": 75,
  "optimization_recommendations": [
    {
      "area": "string",
      "recommendation": "string",
      "expected_improvement": "string"
    }
  ]
}
```
"""

    @staticmethod
    def transcoding_analysis_prompt():
        """Prompt 4: Transcoding configuration analysis"""
        return """
Analyze transcoding configuration and related issues in detail.

ANALYSIS FOCUS:
1. StreamNameGroup Validation:
   - Missing encoding profiles (720p, 360p, 240p, 160p)
   - StreamNameGroup configuration errors
   - Encodes list validation failures
   - Profile mapping inconsistencies

2. Transcoding Pipeline Analysis:
   - Input stream processing
   - Output quality settings validation
   - Adaptive bitrate configuration
   - Multi-resolution setup verification

3. Configuration Issues Detection:
   - Missing or incorrect encoding profiles
   - Bandwidth allocation problems
   - Resolution mapping errors
   - Quality ladder optimization opportunities

4. Setup Recommendations:
   - Optimal transcoding profile configurations
   - Recommended encoding parameters
   - Hardware resource allocation guidelines
   - Implementation best practices

Return JSON format:
```json
{
  "current_config": {
    "available_profiles": ["720p", "360p"],
    "missing_profiles": ["240p", "160p"],
    "configuration_errors": [
      {
        "error": "string",
        "impact": "string",
        "fix": "string"
      }
    ]
  },
  "transcoding_issues": [
    {
      "issue_type": "string",
      "severity": "string",
      "description": "string",
      "affected_streams": ["string"]
    }
  ],
  "optimization_opportunities": [
    {
      "area": "string",
      "current_state": "string",
      "recommended_change": "string",
      "expected_benefit": "string"
    }
  ],
  "recommended_config": {
    "profiles": [
      {
        "resolution": "string",
        "bitrate": "string",
        "codec_settings": {}
      }
    ],
    "settings": {
      "adaptive_bitrate": true,
      "keyframe_interval": 2,
      "quality_ladder": ["string"]
    },
    "implementation_steps": ["string"]
  }
}
```
"""

    @staticmethod
    def timeline_analysis_prompt():
        """Prompt 5: Timeline and pattern analysis"""
        return """
Analyze event timeline and identify patterns in the Wowza logs.

ANALYSIS OBJECTIVES:
1. Timeline Analysis:
   - Chronological sequence of error events
   - Error frequency and distribution over time
   - Peak error periods identification
   - Event clustering and grouping

2. Pattern Recognition:
   - Recurring error patterns and cycles
   - Error sequences and chain reactions
   - Correlation between different events
   - Predictable failure points

3. Temporal Correlation:
   - Time-based relationships between errors
   - Cascade effect identification
   - System recovery patterns
   - Maintenance window impacts

4. Trend Analysis:
   - Error trends over the analyzed period
   - Performance degradation patterns
   - System stability indicators
   - Predictive insights for future issues

Return JSON format:
```json
{
  "timeline": {
    "start_time": "2025-08-21T10:00:00Z",
    "end_time": "2025-08-21T18:00:00Z",
    "total_duration": "8 hours",
    "events_distribution": {
      "morning": 15,
      "afternoon": 32,
      "evening": 8
    }
  },
  "patterns": {
    "recurring_issues": [
      {
        "pattern": "string",
        "frequency": "string",
        "trigger": "string"
      }
    ],
    "error_clusters": [
      {
        "time_range": "string",
        "error_types": ["string"],
        "severity": "string"
      }
    ],
    "peak_periods": ["string"]
  },
  "correlations": [
    {
      "event_a": "string",
      "event_b": "string",
      "correlation_strength": "string",
      "time_offset": "string"
    }
  ],
  "trends": {
    "stability_trend": "improving|degrading|stable",
    "performance_trend": "improving|degrading|stable",
    "predictions": [
      {
        "prediction": "string",
        "confidence": "string",
        "timeframe": "string"
      }
    ]
  }
}
```
"""

    @staticmethod
    def comprehensive_solution_prompt():
        """Prompt 6: Comprehensive solution and implementation plan"""
        return """
Provide comprehensive solutions and implementation plan for all identified issues.

SOLUTION FRAMEWORK:
1. Priority Action Plan:
   - Critical fixes requiring immediate attention
   - High priority issues for next phase
   - Medium/Long-term improvement opportunities
   - Preventive measures to avoid future problems

2. Technical Solutions:
   - Specific configuration changes needed
   - Code or settings modifications
   - Infrastructure adjustments required
   - Third-party integration improvements

3. Implementation Roadmap:
   - Step-by-step implementation guide
   - Resource requirements and dependencies
   - Realistic timeline estimates
   - Risk assessment and mitigation strategies

4. Monitoring and Prevention:
   - Monitoring system setup recommendations
   - Alert configuration guidelines
   - Proactive maintenance procedures
   - Best practices documentation

5. Long-term Strategy:
   - System architecture improvements
   - Scalability planning considerations
   - Performance optimization roadmap
   - Disaster recovery planning

Return JSON format:
```json
{
  "executive_summary": "Brief overview of findings and recommendations",
  "priority_fixes": {
    "critical": [
      {
        "issue": "string",
        "solution": "string",
        "timeline": "immediate",
        "resources_needed": ["string"]
      }
    ],
    "high": ["similar structure"],
    "medium": ["similar structure"]
  },
  "technical_solutions": {
    "config_changes": [
      {
        "component": "string",
        "current_setting": "string",
        "recommended_setting": "string",
        "reason": "string"
      }
    ],
    "code_modifications": ["string"],
    "infrastructure_updates": ["string"]
  },
  "implementation_plan": {
    "phase_1": {
      "duration": "string",
      "tasks": ["string"],
      "dependencies": ["string"]
    },
    "phase_2": {"similar structure"},
    "phase_3": {"similar structure"}
  },
  "monitoring_setup": {
    "metrics_to_track": ["string"],
    "alert_rules": [
      {
        "metric": "string",
        "threshold": "string",
        "action": "string"
      }
    ],
    "dashboards": ["string"]
  },
  "prevention_strategy": {
    "best_practices": ["string"],
    "maintenance_schedule": ["string"],
    "training_needs": ["string"]
  },
  "success_metrics": [
    {
      "metric": "string",
      "target": "string",
      "measurement_method": "string"
    }
  ]
}
```
"""

# Convenience functions for prompt management
def get_prompt(prompt_name):
    """Get prompt by name"""
    prompts = WowzaAnalysisPrompts.get_all_prompts()
    return prompts.get(prompt_name, "Prompt not found")

def get_prompt_names():
    """Get list of all available prompt names"""
    return list(WowzaAnalysisPrompts.get_all_prompts().keys())
